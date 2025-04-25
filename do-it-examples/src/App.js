import logo from './logo.svg'
import './App.css'

function getTitle(title) {
   return title
}
const list = [
   {
      id: 1,
      name: 'Leanne Graham',
      username: 'Bret',
      email: 'Sincere@april.biz',
      phone: '1-770-736-8031 x56442',
      website: 'hildegard.org',
   },
   {
      id: 2,
      name: 'Ervin Howell',
      username: 'Antonette',
      email: 'Shanna@melissa.tv',
      phone: '010-692-6593 x09125',
      website: 'anastasia.net',
   },
]
function List() {
   return list.map(function (item) {
      return (
         <div key={item.id}>
            <span>name: {item.name}</span>
            <br />
            <span>username: {item.username}</span>
            <br />
            <span>email: {item.email}</span>
            <br />
            <span>phone: {item.phone}</span>
            <br />
            <span>
               website:
               <a href={`http://${item.website}`}> {item.website}</a>
            </span>
            <hr />
         </div>
      )
   })
}

class Developer {
   constructor(firstName, lastName) {
      this.firstName = firstName
      this.lastName = lastName
   }
   getName() {
      const date = new Date().toLocaleTimeString()
      return this.firstName + ' ' + this.lastName + '( ' + date + ' )'
   }
}
const robin = new Developer('Robin', 'Wieruch')

function App() {
   let names = ['아 이 디', '비밀번호', '로그인', '다시입력']
   const tableStyle = {
      backgroundColor: '#292929',
      fontSize: '20px',
   }
   const welcome = {
      greeting: 'Hey',
      title: 'React',
   }

   const numbers = [1, 4, 9, 16]
   const newNumbers = numbers.map(function (number) {
      return number * 2
   })
   console.log(newNumbers)
   return (
      <div className="App">
         <div>
            <h1>{robin.getName()}</h1>
         </div>
         <div>
            <h1>
               {welcome.greeting}&nbsp;
               {welcome.title}
            </h1>
            <hr /> <h1>안녕 {getTitle('리액트')}</h1>
         </div>
         <hr />
         <List />
         <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
            <p>
               Edit <code>src/App.js</code> and save to reload.
            </p>
            <a
               className="App-link"
               href="https://reactjs.org"
               target="_blank"
               rel="noopener noreferrer"
            >
               리액트 배우기
            </a>
         </header>

         <form action="home.html" method="get">
            <table border="1" align="center" style={tableStyle}>
               <tr>
                  <td>{names[0]}</td>
                  <td>
                     <input name="id" />
                  </td>
               </tr>
               <tr>
                  <td>{names[1]}</td>
                  <td>
                     <input name="pwd" />
                  </td>
               </tr>
               <tr>
                  <td colSpan="2">
                     <input type="submit" value={names[2]} />
                     <input type="reset" value={names[3]} />
                  </td>
               </tr>
            </table>
         </form>
      </div>
   )
}

export default App
