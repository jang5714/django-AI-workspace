import React, {useState} from 'react'
import styled from 'styled-components'

export default function Todo(){
    const [todo, setTodo] = useState('')
    let val = ''
    const add = e => { //카톡
        e.preventDefault() //이벤트를 막아라
        val = e.target.value
    }
    const del = e => { //카톡
        e.preventDefault() //이벤트를 막아라
        setTodo('')
        }
    const submitForm = e =>{// 엔터 기능
        e.preventDefault()
        setTodo(val)
        document.getElementById('todo-input').value=''
    }

    return (
        <form onSubmit={submitForm} method='POST'>
            <Div>
                <input type='text' id='todo-input' onChange={add}/>
                <input type='submit' value='ADD'/><br/>
                <span>{todo}</span>
                <input type='button' onClick={del} value='DEL'/>
            </Div>
        </form>
    )
}

const Div = styled.div`
    text-align: center;
`