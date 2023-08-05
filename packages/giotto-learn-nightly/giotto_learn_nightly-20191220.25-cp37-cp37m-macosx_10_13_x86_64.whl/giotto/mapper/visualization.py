import logging
import operator
import traceback
from functools import reduce

import numpy as np
import plotly.graph_objects as go
from IPython.display import display
from ipywidgets import Layout, widgets
from matplotlib.cm import get_cmap
from matplotlib.colors import rgb2hex

from .utils._logging import OutputWidgetHandler
from .utils.visualization import (_get_colorscale_buttons, _get_colorscales,
                                  _get_column_color_buttons, _get_node_size,
                                  get_node_summary, _get_node_text,
                                  set_node_sizeref)


def create_network_2d(graph, data, node_pos, node_color,
                      columns_to_color=None, plotly_kwargs=None):
    """
    Parameters
    ----------
    graph : igraph.Graph
        The nerve of the refined pullback cover. Nodes correspond to cluster
        sets, and an edge exists between two nodes if they share at least one
        point in common.

    data : ndarray, shape (n_samples, n_features)
        The point cloud data used to generate the nerve.

    node_pos : igraph.Graph.layout or ndarray, shape (n_nodes, n_dims)
        Encodes the layout of the graph according to a layout algorithm or
        pre-defined array of coordinates in an n-dimensional space.

    node_color : ndarray, shape (n_nodes,)
        The numerical values to color each node of the graph by.

    columns_to_color : dict, optional, default: ``None``
        Key-value pairs (column_name, column_index) to specify which columns of
        :attr:`data` to color the graph by. Generates a dropdown widget to
        select the columns to color by.

    plotly_kwargs : dict, optional, default: ``None``
        Keyword arguments to configure the Plotly Figure.

    Returns
    -------
    fig : ploty.graph_objs.Figure
        The figure representing the nerve (topological graph).
    """
    # TODO: allow custom size reference
    node_elements = graph['node_metadata']['node_elements']
    plot_options = {
        'edge_trace_line': dict(width=0.5, color='#888'),
        'edge_trace_hoverinfo': None,
        'edge_trace_mode': 'lines',
        'node_trace_mode': 'markers',
        'node_trace_hoverinfo': 'text',
        'node_trace_marker_showscale': True,
        'node_trace_marker_colorscale': 'viridis',
        'node_trace_marker_reversescale': False,
        'node_trace_marker_line': dict(width=.5, color='#888'),
        'node_trace_marker_color': node_color,
        'node_trace_marker_size': _get_node_size(node_elements),
        'node_trace_marker_sizemode': 'area',
        'node_trace_marker_sizeref': set_node_sizeref(node_elements),
        'node_trace_marker_sizemin': 4,
        'node_trace_marker_cmin': 0,
        'node_trace_marker_cmax': 1,
        'node_trace_marker_colorbar': dict(thickness=15,
                                           title='',
                                           xanchor='left',
                                           titleside='right'),
        'node_trace_marker_line_width': 2,
        'node_trace_text': _get_node_text(graph),
        'layout_showlegend': False,
        'layout_hovermode': 'closest',
        'layout_margin': {'b': 20, 'l': 5, 'r': 5, 't': 40},
        'layout_xaxis': dict(showgrid=False, zeroline=False,
                             showticklabels=False, ticks="",
                             showline=False),
        'layout_yaxis': dict(showgrid=False, zeroline=False,
                             showticklabels=False, ticks="",
                             showline=False),
        'layout_xaxis_title': "",
        'layout_yaxis_title': ""
    }

    if plotly_kwargs is not None:
        plot_options.update(plotly_kwargs)

    # TODO check we are not losing performance by using map + lambda
    edge_x = list(reduce(operator.iconcat,
                         map(lambda x: [node_pos[x[0]][0],
                                        node_pos[x[1]][0], None],
                             graph.get_edgelist()), []))

    edge_y = list(reduce(operator.iconcat,
                         map(lambda x: [node_pos[x[0]][1],
                                        node_pos[x[1]][1], None],
                             graph.get_edgelist()), []))

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=plot_options['edge_trace_line'],
        hoverinfo=plot_options['edge_trace_hoverinfo'],
        mode=plot_options['edge_trace_mode'])

    node_x = [node_pos[k][0] for k in range(graph.vcount())]
    node_y = [node_pos[k][1] for k in range(graph.vcount())]

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode=plot_options['node_trace_mode'],
        hoverinfo=plot_options['node_trace_hoverinfo'],
        hovertext=plot_options['node_trace_text'],
        marker=dict(
            showscale=plot_options['node_trace_marker_showscale'],
            colorscale=plot_options['node_trace_marker_colorscale'],
            reversescale=plot_options['node_trace_marker_reversescale'],
            line=plot_options['node_trace_marker_line'],
            color=plot_options['node_trace_marker_color'],
            size=plot_options['node_trace_marker_size'],
            sizemode=plot_options['node_trace_marker_sizemode'],
            sizeref=plot_options['node_trace_marker_sizeref'],
            sizemin=plot_options['node_trace_marker_sizemin'],
            cmin=plot_options['node_trace_marker_cmin'],
            cmax=plot_options['node_trace_marker_cmax'],
            colorbar=plot_options['node_trace_marker_colorbar'],
            line_width=plot_options['node_trace_marker_line_width']),
        text=plot_options['node_trace_text'])

    fig = go.FigureWidget(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            showlegend=plot_options['layout_showlegend'],
            hovermode=plot_options['layout_hovermode'],
            margin=plot_options['layout_margin'],
            xaxis=plot_options['layout_xaxis'],
            yaxis=plot_options['layout_yaxis'],
            xaxis_title=plot_options['layout_xaxis_title'],
            yaxis_title=plot_options['layout_yaxis_title'])
    )
    fig.update_layout(template='simple_white', autosize=False)

    # Add dropdown for colorscale of nodes
    column_color_buttons = _get_column_color_buttons(data, node_elements,
                                                     columns_to_color)
    colorscale_buttons = _get_colorscale_buttons(_get_colorscales())

    button_height = 1.1
    fig.update_layout(
        updatemenus=[
            go.layout.Updatemenu(
                buttons=colorscale_buttons,
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.12,
                xanchor='left',
                y=button_height,
                yanchor="top"
            ),
            go.layout.Updatemenu(
                buttons=column_color_buttons,
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.42,
                xanchor='left',
                y=button_height,
                yanchor="top"
            ),
        ])

    fig.update_layout(
        annotations=[
            go.layout.Annotation(text="Colorscale:", x=0, xref="paper",
                                 y=button_height - 0.045, yref="paper",
                                 align="left", showarrow=False)
        ])

    if columns_to_color is not None:
        fig.add_annotation(
            go.layout.Annotation(text="Color by:", x=0.37, xref="paper",
                                 y=button_height - 0.045,
                                 yref="paper", align="left", showarrow=False)

        )

    return fig


def create_network_3d(graph, data, node_pos, node_color, columns_to_color=None,
                      plotly_kwargs=None):
    """
    Parameters
    ----------
    graph : igraph.Graph
        The nerve of the refined pullback cover. Nodes correspond to cluster
        sets, and an edge exists between two nodes if they share at least one
        point in common.

    data : ndarray, shape (n_samples, n_features)
        The point cloud data used to generate the nerve.

    node_pos : igraph.Graph.layout or ndarray, shape (n_nodes, n_dims)
        Encodes the layout of the graph according to a layout algorithm or
        pre-defined array of coordinates in an n-dimensional space.

    node_color : ndarray, shape (n_nodes,)
        The numerical values to color each node of the graph by.

    columns_to_color : dict, optional, default: ``None``
        Key-value pairs (column_name, column_index) to specify which columns of
        :attr:`data` to color the graph by. Generates a dropdown widget to
        select the columns to color by.

    plotly_kwargs : dict, optional, default: ``None``
        Keyword arguments to configure the Plotly Figure.

    Returns
    -------
    fig : ploty.graph_objs.Figure
        The figure representing the nerve (topological graph).
    """
    node_elements = graph['node_metadata']['node_elements']
    plot_options = {
        'edge_trace_mode': 'lines',
        'edge_trace_line': dict(color='rgb(125,125,125)',
                                width=1),
        'edge_trace_hoverinfo': 'none',
        'node_trace_mode': 'markers',
        'node_trace_hoverinfo': 'text',
        'node_trace_hoverlabel': dict(
            bgcolor=list(map(lambda x: rgb2hex(get_cmap('viridis')(x)),
                             node_color))),
        'node_trace_marker_showscale': True,
        'node_trace_marker_colorscale': 'viridis',
        'node_trace_marker_reversescale': False,
        'node_trace_marker_line': dict(width=.5, color='#888'),
        'node_trace_marker_color': node_color,
        'node_trace_marker_size': _get_node_size(node_elements),
        'node_trace_marker_sizemode': 'area',
        'node_trace_marker_sizeref': set_node_sizeref(node_elements),
        'node_trace_marker_sizemin': 4,
        'node_trace_marker_cmin': 0,
        'node_trace_marker_cmax': 1,
        'node_trace_marker_colorbar': dict(thickness=15,
                                           title='',
                                           xanchor='left',
                                           titleside='right'),
        'node_trace_marker_line_width': 2,
        'node_trace_text': _get_node_text(graph),
        'axis': dict(showbackground=False,
                     showline=False,
                     zeroline=False,
                     showgrid=False,
                     showticklabels=False,
                     title=''),
        'layout_title': "",
        'layout_width': 750,
        'layout_height': 750,
        'layout_showlegend': False,
        'layout_margin': dict(t=100),
        'layout_hovermode': 'closest',
        'layout_annotations': []
    }

    plot_options['layout_scene'] = dict(xaxis=dict(plot_options['axis']),
                                        yaxis=dict(plot_options['axis']),
                                        zaxis=dict(plot_options['axis']))

    if plotly_kwargs is not None:
        plot_options.update(plotly_kwargs)

    edge_x = list(reduce(operator.iconcat,
                         map(lambda x: [node_pos[x[0]][0],
                                        node_pos[x[1]][0], None],
                             graph.get_edgelist()), []))
    edge_y = list(reduce(operator.iconcat,
                         map(lambda x: [node_pos[x[0]][1],
                                        node_pos[x[1]][1], None],
                             graph.get_edgelist()), []))

    edge_z = list(reduce(operator.iconcat,
                         map(lambda x: [node_pos[x[0]][2],
                                        node_pos[x[1]][2], None],
                             graph.get_edgelist()), []))

    edge_trace = go.Scatter3d(x=edge_x,
                              y=edge_y,
                              z=edge_z,
                              mode=plot_options['edge_trace_mode'],
                              line=plot_options['edge_trace_line'],
                              hoverinfo=plot_options['edge_trace_hoverinfo'])

    node_x = [node_pos[k][0] for k in range(graph.vcount())]
    node_y = [node_pos[k][1] for k in range(graph.vcount())]
    node_z = [node_pos[k][2] for k in range(graph.vcount())]

    node_trace = go.Scatter3d(
        x=node_x,
        y=node_y,
        z=node_z,
        mode=plot_options['node_trace_mode'],
        hoverinfo=plot_options['node_trace_hoverinfo'],
        hoverlabel=plot_options['node_trace_hoverlabel'],
        marker=dict(
            showscale=plot_options['node_trace_marker_showscale'],
            colorscale=plot_options['node_trace_marker_colorscale'],
            reversescale=plot_options['node_trace_marker_reversescale'],
            line=plot_options['node_trace_marker_line'],
            color=plot_options['node_trace_marker_color'],
            size=plot_options['node_trace_marker_size'],
            sizemode=plot_options['node_trace_marker_sizemode'],
            sizeref=plot_options['node_trace_marker_sizeref'],
            sizemin=plot_options['node_trace_marker_sizemin'],
            cmin=plot_options['node_trace_marker_cmin'],
            cmax=plot_options['node_trace_marker_cmax'],
            colorbar=plot_options['node_trace_marker_colorbar'],
            line_width=plot_options['node_trace_marker_line_width']),
        text=plot_options['node_trace_text'])

    layout = go.Layout(
        title=plot_options['layout_title'],
        width=plot_options['layout_width'],
        height=plot_options['layout_height'],
        showlegend=plot_options['layout_showlegend'],
        scene=plot_options['layout_scene'],
        margin=plot_options['layout_margin'],
        hovermode=plot_options['layout_hovermode'],
        annotations=plot_options['layout_annotations'])

    fig = go.Figure(data=[edge_trace, node_trace], layout=layout)

    # Add dropdown for colorscale of nodes
    column_color_buttons = _get_column_color_buttons(data, node_elements,
                                                     columns_to_color)
    colorscale_buttons = _get_colorscale_buttons(_get_colorscales())

    button_height = 1.1
    fig.update_layout(
        updatemenus=[
            go.layout.Updatemenu(
                buttons=colorscale_buttons,
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.12,
                xanchor='left',
                y=button_height,
                yanchor="top"
            ),
            go.layout.Updatemenu(
                buttons=column_color_buttons,
                direction="down",
                pad={"r": 10, "t": 10},
                showactive=True,
                x=0.42,
                xanchor='left',
                y=button_height,
                yanchor="top"
            ),
        ])

    fig.update_layout(
        annotations=[
            go.layout.Annotation(text="Colorscale:", x=0, xref="paper",
                                 y=button_height - 0.03, yref="paper",
                                 align="left", showarrow=False)
        ],
        autosize=False
    )

    if columns_to_color is not None:
        fig.add_annotation(
            go.layout.Annotation(text="Color by:", x=0.37, xref="paper",
                                 y=button_height - 0.03,
                                 yref="paper", align="left", showarrow=False)
        )

    return fig


def create_interactive_network(pipe, data, node_pos=None, node_color=None,
                               columns_to_color=None, plotly_kwargs=None,
                               summary_stat=np.mean):
    """
    Parameters
    ----------
    pipe : MapperPipeline
        The nerve of the refined pullback cover. Nodes correspond to cluster
        sets, and an edge exists between two nodes if they share at least one
        point in common.

    data : ndarray, shape (n_samples, n_features)
        The point cloud data used to generate the nerve.

    node_pos : igraph.Graph.layout or ndarray, shape (n_nodes, n_dims)
        Encodes the layout of the graph according to a layout algorithm or
        pre-defined array of coordinates in an n-dimensional space.

    node_color : ndarray, shape (n_nodes,)
        The numerical values to color each node of the graph by.

    columns_to_color : dict, optional, default: ``None``
        Key-value pairs (column_name, column_index) to specify which columns of
        :attr:`data` to color the graph by. Generates a dropdown widget to
        select the columns to color by.

    plotly_kwargs : dict, optional, default: ``None``
        Keyword arguments to configure the Plotly Figure.

    summary_stat : callable, default ``np.mean``
        Summary statistic to apply to the elements in each node of the
        topological graph.
    """
    # TODO could abstract away common patterns in get_cover_params_widgets and
    #  get_cluster_params_widgets

    # TODO allow dimension to be passed as either 2 or 3 as an arg or kwarg
    def get_cover_params_widgets(param, value):
        if isinstance(value, float):
            return (param, widgets.FloatSlider(
                value=value,
                step=0.05,
                min=0.05,
                max=1.0,
                description=param.split('__')[1],
                disabled=False
            ))
        elif isinstance(value, int):
            return (param, widgets.IntSlider(
                value=value,
                min=1,
                max=100,
                step=1,
                description=param.split('__')[1],
                disabled=False
            ))
        else:
            return None

    def get_cluster_params_widgets(param, value):
        if isinstance(value, float):
            return (param, widgets.FloatText(
                    value=value,
                    step=0.1,
                    description=param.split('__')[1],
                    disabled=False
                    ))
        elif isinstance(value, int):
            return (param, widgets.IntText(
                value=value,
                step=1,
                description=param.split('__')[1],
                disabled=False
            ))
        elif isinstance(value, str):
            return (param, widgets.Text(
                value=value,
                description=param.split('__')[1],
                disabled=False
            ))
        else:
            return None

    def update_figure(old_figure, new_figure):
        # TODO could this be abstracted to node and edge traces and metadata
        #  information without need for creating a full new figure object
        old_figure.data[0].x = new_figure.data[0].x
        old_figure.data[0].y = new_figure.data[0].y
        old_figure.data[1].x = new_figure.data[1].x
        old_figure.data[1].y = new_figure.data[1].y
        old_figure.data[1].marker.size = new_figure.data[1].marker.size
        old_figure.data[1].marker.color = new_figure.data[1].marker.color
        old_figure.data[1].marker.sizeref = new_figure.data[1].marker.sizeref

    def get_figure(pipe, data, node_pos, node_color, columns_to_color,
                   summary_stat):
        graph = pipe.fit_transform(data)
        node_elements = graph['node_metadata']['node_elements']
        if node_pos is None:
            node_pos = graph.layout('kamada_kawai')

        if node_color is None:
            node_color = get_node_summary(node_elements, data,
                                          summary_stat=summary_stat)

        return create_network_2d(graph, data, node_pos, node_color,
                                 columns_to_color, plotly_kwargs)

    def response_numeric(change):
        # TODO: remove hardcoding of keys and mimic what is done with clusterer
        handler.clear_logs()
        try:
            pipe.set_mapper_params(
                cover__n_intervals=cover_params_widgets['cover__n_intervals']
                .value)
            pipe.set_mapper_params(
                cover__overlap_frac=cover_params_widgets['cover__overlap_frac']
                .value)

            for param, value in cluster_params.items():
                if isinstance(value, (int, float)):
                    pipe.set_mapper_params(
                        **{param: cluster_params_widgets[param].value}
                    )

            # TODO check this alternative:
            #
            # num_params = {param: value for param, value in
            #               cluster_params.items()
            #               if isinstance(value, (int, float))}
            #
            # pipe.set_mapper_params(
            #     **{param: cluster_params_widgets[param].value for param in
            #        num_params}
            # )

            new_fig = get_figure(pipe, data, node_pos,
                                 node_color, columns_to_color, summary_stat)

            logger.info("Updating figure ...")
            with fig.batch_update():
                update_figure(fig, new_fig)
            valid.value = True
        except Exception:
            exception_data = traceback.format_exc().splitlines()
            logger.exception(exception_data[-1])
            valid.value = False

    def response_text(text):
        handler.clear_logs()
        try:
            for param, value in cluster_params.items():
                if isinstance(value, str):
                    pipe.set_mapper_params(
                        **{param: cluster_params_widgets[param].value}
                    )

            new_fig = get_figure(pipe, data, node_pos,
                                 node_color, columns_to_color, summary_stat)

            logger.info("Updating figure ...")
            with fig.batch_update():
                update_figure(fig, new_fig)
            valid.value = True
        except Exception:
            exception_data = traceback.format_exc().splitlines()
            logger.exception(exception_data[-1])
            valid.value = False

    def observe_numeric_widgets(params, widgets):
        for param, value in params.items():
            if isinstance(value, (int, float)):
                widgets[param].observe(response_numeric, names='value')

    # define output widget to capture logs
    out = widgets.Output()

    @out.capture()
    def click_box(change):
        if logs_box.value:
            out.clear_output()
            handler.show_logs()
        else:
            out.clear_output()

    # initialise logging
    logger = logging.getLogger(__name__)
    handler = OutputWidgetHandler()
    handler.setFormatter(logging.Formatter(
        '%(asctime)s  - [%(levelname)s] %(message)s'))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

    # initialise cover and cluster dictionaries of parameters and widgets
    cover_params = dict(filter(lambda x: x[0].startswith('cover'),
                               pipe.get_mapper_params().items()))
    cover_params_widgets = dict(
        filter(None, map(lambda x: get_cover_params_widgets(*x),
                         cover_params.items())))
    cluster_params = dict(filter(lambda x: x[0].startswith('clusterer'),
                                 pipe.get_mapper_params().items()))
    cluster_params_widgets = dict(
        filter(None, map(lambda x: get_cluster_params_widgets(*x),
                         cluster_params.items())))

    # create button for text inputs
    submit_button = widgets.Button(description="Submit")
    submit_button.on_click(response_text)

    # initialise widgets for validating input parameters of pipeline
    valid = widgets.Valid(
        value=True,
        description='Valid parameters',
        style={'description_width': '100px'},
    )

    # initialise widget for showing the logs
    logs_box = widgets.Checkbox(
        description='Show logs: ',
        value=False,
        indent=False
    )

    # initialise figure with initial pipeline and config
    if plotly_kwargs is None:
        plotly_kwargs = dict()

    fig = get_figure(pipe, data, node_pos, node_color,
                     columns_to_color, summary_stat)

    observe_numeric_widgets(cover_params, cover_params_widgets)
    observe_numeric_widgets(cluster_params, cluster_params_widgets)

    logs_box.observe(click_box, names='value')

    # define containers for input widgets
    container_cover = widgets.HBox(children=list(
        cover_params_widgets.values()))

    container_cluster_text = widgets.HBox(
        children=list(v for k, v in cluster_params_widgets.items()
                      if isinstance(cluster_params[k], str)) + [submit_button])

    container_cluster_layout = Layout(display='flex', flex_flow='row wrap')

    container_cluster_numeric = widgets.HBox(
        children=list(v for k, v in cluster_params_widgets.items()
                      if isinstance(cluster_params[k], (int, float))
                      ), layout=container_cluster_layout
    )

    box = widgets.VBox([container_cover, container_cluster_text,
                        container_cluster_numeric, fig,
                        valid, logs_box])
    display(box, out)
