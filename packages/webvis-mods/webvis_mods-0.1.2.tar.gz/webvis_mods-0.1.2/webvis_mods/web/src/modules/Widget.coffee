import React, { Component } from 'react'
import L from 'react-dom-factories'
L_ = React.createElement

export default Widget = (props, children)->
  {onDelete} = props
  L.div className:'widget', key:props.key,
    L.div
      className:'delete-card'
      onClick:onDelete
      'x'
    children
 
