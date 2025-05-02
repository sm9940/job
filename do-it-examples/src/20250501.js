import React, { useState } from 'react'
// import ReactDOM from 'react' → 사용되지 않음, 삭제 가능
import logo from './logo.svg' // 사용 안됨
import './App.css' // 스타일 사용 시 필요

const App = () => {
   // 리스트 예제: 사용 안되고 있음
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

   // 초기 스토리 데이터
   const initialStories = [
      {
         title: 'React',
         url: 'https://reactjs.org/',
         author: 'Jordan Walke',
         num_comments: 3,
         points: 4,
         objectID: 0,
      },
      {
         title: 'Redux',
         url: 'https://redux.js.org/',
         author: 'Dan Abramov, Andrew Clark',
         num_comments: 2,
         points: 5,
         objectID: 1,
      },
   ]
   const getAsyncStories = () => {
      Promise.resolve({ data: { stories: initialStories } })
   }
   const [stories, setStories] = React.useState(initialStories)
   // React.useEffect(() => {
   //    getAsyncStories().then((result) => {
   //       setStories(result.data.stories)
   //    })
   // }, [])
   const handleRemoveStory = (item) => {
      const newStories = stories.filter((story) => item.objectID !== story.objectID)
      setStories(newStories)
   }
   // Search 컴포넌트: 사용자 입력을 받고, 상위 컴포넌트의 핸들러를 실행
   const Search = (props) => {
      const [searchTerm, setSearchTerm] = React.useState('') // 내부 상태 (사용되지 않음)

      const handleChange = (event) => {
         props.onSearch(event) // 부모 컴포넌트로 검색어 전달
      }

      return (
         <div>
            <label htmlFor="search">Search: </label>
            <input id="search" type="text" onChange={props.onSearch} />

            <p>
               Searching for <strong>{searchTerm}</strong>.
            </p>
         </div>
      )
   }

   // List 컴포넌트: 리스트 데이터를 받아 각 항목을 Item 컴포넌트로 출력
   const List = ({ list, onRemoveItem }) =>
      list.map((item) => <Item key={item.objectID} item={item} onRemoveItem={onRemoveItem} />)

   // Item 컴포넌트: 하나의 스토리 항목을 출력
   const Item = ({ item, onRemoveItem }) => {
      const handleRemoveItem = () => {
         onRemoveItem(item)
      }
      return (
         <div>
            <span>
               <a href={item.url}>{item.title}</a>
            </span>
            <span>{item.author}</span>
            <span>{item.num_comments}</span>
            <span>{item.points}</span>
            <button type="button" onClick={handleRemoveItem}>
               Dismiss
            </button>
         </div>
      )
   }

   // useSemiPersistentState: 로컬스토리지와 연동되는 커스텀 훅
   const useSemiPersistentState = (key, initializeState) => {
      const [value, setValue] = React.useState(localStorage.getItem(key) || initializeState)

      // 값이 변경될 때 로컬스토리지에 저장
      React.useEffect(() => {
         localStorage.setItem(key, value)
         console.log(key)
         console.log(value)
      }, [value, key])

      return [value, setValue]
   }

   // 검색어 상태: 'search'라는 키로 로컬스토리지와 동기화
   const [searchTerm, setSearchTerm] = useSemiPersistentState('search', 'React')

   // 검색 핸들러: input의 변경 값을 상태에 반영
   const handleSearch = (event) => {
      setSearchTerm(event.target.value)
   }

   // InputWithLabel: 라벨과 입력창이 함께 있는 커스텀 input 컴포넌트
   const InputWithLabel = ({
      id,
      children,
      value,
      type = 'text',
      isFocused, // true면 자동 포커스
      onInputChange,
   }) => {
      const inputRef = React.useRef()

      // isFocused가 true일 경우 input에 자동 포커스
      React.useEffect(() => {
         if (isFocused && inputRef.current) {
            inputRef.current.focus()
         }
      }, [isFocused])

      return (
         <>
            <label htmlFor={id}>{children}</label>
            &nbsp;
            <input
               ref={inputRef}
               id={id}
               type={type}
               value={value}
               autoFocus={isFocused}
               onChange={onInputChange}
            />
         </>
      )
   }

   // 검색어가 포함된 스토리만 필터링
   const searchStories = stories.filter(function (story) {
      return story.title.toLowerCase().includes(searchTerm.toLowerCase())
   })

   // 최종 렌더링
   return (
      <div>
         <h1>My Hacker Stories</h1>
         {/* 아래 주석처럼 Search 컴포넌트를 사용하도록 구조 변경 가능 */}
         {/* <Search search={searchTerm} onSearch={handleSearch}/> */}
         {/* 직접 InputWithLabel을 사용 중 */}
         <InputWithLabel
            id="search"
            label="Search"
            value={searchTerm}
            onInputChange={handleSearch}
            isFocused
         >
            <strong>검색 : </strong>
         </InputWithLabel>
         <hr />
         list
         {/* 필터링된 스토리 리스트 출력 */}
         <List list={searchStories} onRemoveItem={handleRemoveStory} />
      </div>
   )
}

export default App
