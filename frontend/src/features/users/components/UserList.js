import axios from 'axios';
import React, { useEffect, useState } from 'react';
import { UserListForm } from '..';


export default function UserList() {
  const [list, setList] = useState([])
  const SERVER = 'http://localhost:8000/api'
 
  const userList = () => {
      userList()
      axios.get(`${SERVER}/users/list`)
      alert('리스트 성공')
      .then(res => setList(res.data) )
      .catch(err => 
        alert('리스트 실패')
        .console.log(err))
  }

  useEffect(() =>{
    userList() 
  }, [])

  return (
    <div>
      <h1>사용자 목록</h1>
      <UserListForm list={list}/>
    </div>
  );
}