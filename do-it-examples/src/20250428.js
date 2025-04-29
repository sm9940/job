import React from 'react'
import './App.css'

function login() {
   function go() {
      var id = document.getElementsByName('id')
      if (id.value) {
      }
   }
   return (
      <form id="loginf">
         <table>
            <tr>
               <td>
                  <label for="id">계정</label>
               </td>
               <td>
                  <input type="text" id="id" name="id" />
               </td>
            </tr>
            <tr>
               <td>
                  <label for="passwd">패스워드</label>
               </td>
               <td>
                  <input type="password" id="password" name="password" />
               </td>
            </tr>
            <tr>
               <td>
                  <input
                     type="button"
                     id="loginb"
                     name="loginb"
                     value="로그인"
                     //  onClick= {return go();}
                  />
               </td>
               <td>
                  <div id="result"></div>
               </td>
            </tr>
         </table>
      </form>
   )
}
export default login
