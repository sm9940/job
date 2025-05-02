import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import App from './App'
import reportWebVitals from './reportWebVitals'
import Main from './component/main'
import Header from './component/header'
import Footer from './component/footer'
import Product from './component/product'
import NotFound from './component/notFound'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'

const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(
   <Router>
      <Header />
      <Routes>
         <Route path="/" element={<Main />}></Route>
         <Route path="/product/:productId" element={<Product />}></Route>
         <Route path="*" element={<NotFound />}></Route>
      </Routes>
      <Footer />
   </Router>
)

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals()
