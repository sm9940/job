import React from 'react'
import ReactDOM from 'react'
import logo from './logo.svg'
import './App.css'
const App = () => {
   const users = [
      {
         id: 1,
         name: 'Leanne Graham',
         password: '1234',
         email: 'Sincere@april.biz',
         phone: '1-770-736-8031 x56442',
         website: 'hildegard.org',
      },
      {
         id: 2,
         name: 'Ervin Howell',
         password: '0000',
         email: 'Shanna@melissa.tv',
         phone: '010-692-6593 x09125',
         website: 'anastasia.net',
      },
   ]
   const [loginTerm, setloginTerm] = React.useState('')
   const [passwordTerm, setPasswordTerm] = React.useState('id first')
   const handleSearch = (event) => {
      event.target === document.getElementById('email')
         ? setloginTerm(event.target.value)
         : setPasswordTerm(event.target.value)
      // console.log(event.target.value)
   }
   const searchStories = users.filter(function (story) {
      return (
         story.email.toLowerCase() === loginTerm.toLowerCase() && story.password === passwordTerm
      )
   })
   return (
      <div>
         <h1>My Hacker Stories</h1>
         <Search onSearch={handleSearch} />

         <hr />
         <List list={searchStories} />
      </div>
   )
}

const Search = (props) => (
   <div>
      <label htmlFor="search">Login: </label>
      <input id="email" type="text" onChange={props.onSearch} />
      <br />
      <label htmlFor="search">password: </label>
      <input id="password" type="text" onChange={props.onSearch} />
   </div>
)
// 로그인 처리시 사용자 정보 출력
const List = ({ props }) =>
   props.list.map((item) => (
      <div key={item.id}>
         <span>
            <a href={item.website}>{item.website}</a>
         </span>
         <br />
         <span>{item.phone}</span>
         <br />
         <span>{item.name}</span>
         <br />
      </div>
   ))

export default App
