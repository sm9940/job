import React, { useState } from 'react'
import { Link } from 'react-router-dom'

function Main(props) {
   const [timer, setTimer] = useState('00:00:00')

   const currentTimer = () => {
      const date = new Date()
      const hours = String(date.getHours()).padStart(2, '0')
      const minutes = String(date.getMinutes()).padStart(2, '0')
      const seconds = String(date.getSeconds()).padStart(2, '0')
      setTimer(`${hours}:${minutes}:${seconds}`)
   }
   const startTimer = () => {
      setInterval(currentTimer, 1000)
   }
   startTimer()
   return (
      <div>
         <main>
            <h1>메인</h1>
            <h2>{timer}</h2>
            <ul>
               <Link to="/product/1">
                  <li>과자</li>
               </Link>
               <Link to="/product/2">
                  <li>음료수</li>
               </Link>
            </ul>
         </main>
      </div>
   )
}
export default Main
