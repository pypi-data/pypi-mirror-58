// Copyright (c) Juelich Supercomputing Centre (JSC)
// Distributed under the terms of the Modified BSD License.

import {
  DOMWidgetModel, DOMWidgetView, ISerializers
} from '@jupyter-widgets/base';

import {
  MODULE_NAME, MODULE_VERSION
} from './version';

// Import the CSS
import '../css/widget.css'

import SmartConnect from 'wslink/src/SmartConnect';
import RemoteRenderer from 'paraviewweb/src/NativeUI/Canvas/RemoteRenderer';
import SizeHelper from 'paraviewweb/src/Common/Misc/SizeHelper';
import ParaViewWebClient from 'paraviewweb/src/IO/WebSocket/ParaViewWebClient';


export
class RemoteRendererModel extends DOMWidgetModel {
  defaults() {
    return {...super.defaults(),
      _model_name: RemoteRendererModel.model_name,
      _model_module: RemoteRendererModel.model_module,
      _model_module_version: RemoteRendererModel.model_module_version,
      _view_name: RemoteRendererModel.view_name,
      _view_module: RemoteRendererModel.view_module,
      _view_module_version: RemoteRendererModel.view_module_version,
    };
  }

  static serializers: ISerializers = {
      ...DOMWidgetModel.serializers,
    }

  static model_name = 'RemoteRendererModel';
  static model_module = MODULE_NAME;
  static model_module_version = MODULE_VERSION;
  static view_name = 'RemoteRendererView';   
  static view_module = MODULE_NAME;
  static view_module_version = MODULE_VERSION;
}


export
class RemoteRendererView extends DOMWidgetView {
  render() {
    this.el.classList.add('custom-widget');

    var that = this;
    
    // div to hold the canvas of the RemoteRenderer.
    var render_div = document.createElement('div');
    render_div.style.height = '100%';
    render_div.style.width = '100%';
    this.el.appendChild(render_div);

    /* Get configuration for SmartConnect.
    *  SmartConnect will establish a direct
    *  WebSocket connection using Autobahn. 
    */
    var config = {
      sessionURL: this.model.get('sessionURL'),
      secret: this.model.get('authKey')
    };
    var smartConnect = SmartConnect.newInstance({ config: config });

    smartConnect.onConnectionReady(function (connection: any) {
      // Create the RemoteRenderer
      var pvwClient = ParaViewWebClient.createClient(connection, [
        'MouseHandler',
        'ViewPort',
        'ViewPortImageDelivery']
      );
      var renderer = new RemoteRenderer(pvwClient);
      renderer.setContainer(render_div);
      renderer.setView(that.model.get('viewID'));
      renderer.onImageReady(function () {
        // Resize when the renderer is placed within a widget.
        if (that.el.style.width != '100%') {
          that.el.style.width = '100%';
          renderer.resize();
        }
        console.log("We are good.");
      });

      // Handle size changes when the entire window is resized.
      SizeHelper.onSizeChange(function () {
        renderer.resize();
      });
      SizeHelper.startListening();

      // Explicit render called from python side.
      that.model.on('change:_update', function () {
        renderer.render(true);
      }, that);
    });

    smartConnect.connect();
  }
}
