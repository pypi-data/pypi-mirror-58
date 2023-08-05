// Copyright (c) Jupyter Development Team.
// Distributed under the terms of the Modified BSD License.

import expect = require('expect.js');

import {
  // Add any needed widget imports here (or from controls)
} from '@jupyter-widgets/base';

import {
  createTestModel
} from './utils.spec';

import {
  RemoteRendererModel, RemoteRendererView
} from '../../src/'


describe('RemoteRenderer', () => {

  describe('RemoteRendererModel', () => {

    it('should be createable', () => {
      let model = createTestModel(RemoteRendererModel);
      expect(model).to.be.an(RemoteRendererModel);
      expect(model.get('sessionURL')).to.be('ws://localhost:8080/ws');
    });

    it('should be createable with a value', () => {
      let state = { sessionURL: 'Foo Bar!' }
      let model = createTestModel(RemoteRendererModel, state);
      expect(model).to.be.an(RemoteRendererModel);
      expect(model.get('sessionURL')).to.be('Foo Bar!');
    });

  });

});