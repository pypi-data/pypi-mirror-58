import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement

import Notebook from './modules/notebook.coffee'
import Visualiser from './modules/visualiser.coffee'
import WSwrap from './modules/ws.coffee'
import ResponsiveGL from './modules/ResponsiveStorageGrid.coffee'
import {Responsive, WidthProvider} from 'react-grid-layout'

import Button from './modules/UIcomponents/button.coffee'
import Widget from './modules/Widget.coffee'

import FuncChainer from './modules/helpers/funchainer.coffee'
import LocalStorage from './modules/helpers/localStorage.coffee'
import {get_nb_name} from './modules/helpers/argparser.coffee'
import {parse_message} from './Data/interface.coffee'

import './styles/grid.css'
import './styles/widget.less'
import './styles/graph.less'
import './styles/misc.less'

visStorage = new LocalStorage key:'webvis'

defaultVars = [
       name:'dummyvar', value:'hello world'
    ]

export default class App extends React.Component
  state: {}
  constructor:->
    super()
    @state.vars = visStorage.get('vars') or defaultVars

  onWsMessage: (msg)=>
      new_var = parse_message msg.data

      @setState (s,p)->
        s.vars = s.vars.map (v)->
          if (v.name==new_var.name) then new_var else v
        s

  nameChange: (id)->(name)=>
    console.log 'namechange'
    @setState (s,p)->
      s.vars[id].name = name
      visStorage.save 'vars', s.vars
      s
    console.log @state
  addWidget: ()=>
    new_var = name:'New variable',value:'Nothing here yet'
    @setState (s,p)->
      s.vars.push new_var
      visStorage.save 'vars', s.vars
      s
  deleteWidget: (id)->()=>
    console.log "Deleting widget #{id}"
    @setState (s,p)->
      console.log s.vars
      s.vars.splice id, 1
      visStorage.save 'vars', s.vars
      s

  onConnect:(ws)=>
    @connected = true
    f = ()=>
      names = @state.vars.map (v)->v.name
      msg = command:'setvars', params: names
      ws.send  JSON.stringify msg
      if @connected
        setTimeout f, 4000
    f()
  onDisconnect:()=>
    @connected = false

  render: ->
    L.div className:'app',
      L.div className:'top-bar',
        L_ WSwrap,
          className:'inline'
          onMessage:@onWsMessage
          onConnect: @onConnect
          onDisconnect: @onDisconnect
        L_ Button,
          className:'add-widget'
          text:'Add widget'
          onPress:@addWidget
      L_ ResponsiveGL,
        className:'grid'
        draggableCancel:"input"
        L.div key:'notebook', L_ Notebook, nb_name:get_nb_name()
        for v,idx in @state.vars
          Widget
            onDelete:@deleteWidget idx
            key:'vis'+idx
            L_ Visualiser,
              variable: v
              onNameChange:@nameChange idx
