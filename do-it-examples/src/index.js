import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import App from './App'
import reportWebVitals from './reportWebVitals'
import Login from './20250428'
import Tues from './20250429'
import Weds from './20250430'
import Thurs from './20250501'
const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(
   <div>
      <React.StrictMode>
         <Thurs />
      </React.StrictMode>
      {/* <Login /> */}
      {/* <Tues /> */}
   </div>
)

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals()
