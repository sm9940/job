import logo from './logo.svg'
import './App.css'

function App() {
   return (
      <div className="App">
         <h1>My Hacker Stories</h1>
         <a href="http://localhost:8000">hello</a>
         <form method="get" action="http://localhost:8000/items/2">
            <input name="q"></input>
         </form>
      </div>
   )
}

export default App
