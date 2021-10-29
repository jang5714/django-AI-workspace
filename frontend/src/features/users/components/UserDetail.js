import React, { useState, useEffect, useCallback} from 'react';
import { Link, useHistory } from 'react-router-dom';
import axios from 'axios';


export default function UserDetail() {
    const SERVER = 'http://localhost:8000/api'
    const history = useHistory()
    const [detail, setDetail] = useState({
        username:'', name:'', birth:'', address:'', email:'', password:''
    })
    const headers = {
        'Content-Type' : 'application/json',
        'Authorization': 'JWT fefege..'
      }
    const fetchOne = () => {
        const sessionUser = JSON.parse(localStorage.getItem('sessionUser'))
        alert('사용자 아이디: ' +sessionUser.username)
        axios.post(`${SERVER}/users/detail` , JSON.stringify(sessionUser),{headers}) 
        .then(res => {
            alert(`회원 정보 조회 성공 : ${res.data}`)
            setDetail(res.data)
        })
        .catch(err => {
            alert(`${err}`)
        })
    }
    useEffect(() => {
        fetchOne()
    }, [])

    const logout = e => {
        e.preventDefault()
        localStorage.setItem('sessionUser','')
        history.push('/')
    }
    
  return (
    <div>
        <h1>회원 정보</h1>

        <ul>
            <li>
                <label>
                    <span>아이디: {detail.username}</span>
                </label>
            </li>
            <li>
                <label>
                <span>email: {detail.email}</span>
                </label>
            </li>
            <li>
                <label>
                <span>비밀번호: *******</span>
                </label>
            </li>
            <li>
                <label>
                <span>이름: {detail.name}</span>
                </label>
            </li>
            <li>
                <input type="button" value="회원정보수정" onClick={()=> history.push('/users/modify')}/>
            </li>
            <li>
                <input type="button" value="로그아웃" onClick={logout}/>
            </li>
        </ul>
    </div>
  );
}
