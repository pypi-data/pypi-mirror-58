#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Juelich Supercomputing Centre (JSC).
# Distributed under the terms of the Modified BSD License.

"""
This module creates a ParaView-Web RemoteRenderer Widget in the output area below a cell in a Jupyter Notebook. This requires a VTK-Web or ParaView-Web server, see https://kitware.github.io/paraviewweb/examples/RemoteRenderer.html#RemoteRenderer.

Example:
    Start a ParaView-Web server with
    ```
    $ pvpython pv_server.py --port 8080 --authKey wslink-secret
    ```

    In the notebook, display the RemoteRenderer Widget with
    ```
    display(pvlink.RemoteRenderer(sessionURL='ws://localhost:8080/ws', authKey='wslink-secret'))
    ```
"""

from ipywidgets import DOMWidget
from traitlets import Int, Unicode
from ._frontend import module_name, module_version


class RemoteRenderer(DOMWidget):
    """A ParaView-Web RemoteRenderer Widget.

    It must be used with a VTK-Web or ParaView-Web server,
    see https://kitware.github.io/paraviewweb/examples/RemoteRenderer.html#RemoteRenderer.
    """
    _model_name = Unicode('RemoteRendererModel').tag(sync=True)
    _model_module = Unicode(module_name).tag(sync=True)
    _model_module_version = Unicode(module_version).tag(sync=True)
    _view_name = Unicode('RemoteRendererView').tag(sync=True)
    _view_module = Unicode(module_name).tag(sync=True)
    _view_module_version = Unicode(module_version).tag(sync=True)

    sessionURL = Unicode('ws://localhost:8080/ws').tag(sync=True)
    authKey = Unicode('wslink-secret').tag(sync=True)
    viewID = Unicode("-1").tag(sync=True)
    # Placeholder to force rendering updates on change.
    _update = Int(0).tag(sync=True)


    def __init__(self, sessionURL='ws://localhost:8080/ws', authKey='wslink-secret', viewID='-1', *args, **kwargs):
        """Args:
            sessionURL (str): URL where the webserver is running.
            authKey (str): Authentication key for clients to connect to the WebSocket.
            viewID (str): ViewID of the view to connect to (only relevant if multiple views exist on the server side).
        """
        super(RemoteRenderer, self).__init__(*args, **kwargs)
        self.sessionURL = sessionURL
        self.authKey = authKey
        self.viewID = viewID


    def update_render(self):
        """Explicit call for the renderer on the javascript side to render."""
        self._update += 1