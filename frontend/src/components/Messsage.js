import React from 'react'
import { Alert } from 'react-bootstrap'

function Messsage({variant, children}) {
  return (
    <Alert variant={variant}>
{children}
    </Alert>
  )
}

export default Messsage
