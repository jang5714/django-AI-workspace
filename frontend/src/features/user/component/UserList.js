import react from 'react'
import styled from 'styled-components'
import { useSelector, useDispatch } from 'react-redux'
import { toggleUserAction, deleteUserAction } from 'features/user/modules/userSlice'


export default function UserList(){
    const users = useSelector( state => state.userReducer.users)
    const dispatch = useDispatch()
    const deleteUser = id => dispatch(deleteUserAction(id))
    return(
        <Div>
            {users.length === 0 && (<h1>등록된 유저가 없습니다</h1>)}
            {users.length !== 0 && (<h1>{users.length}개의 유저가 있습니다</h1>)}
            {users.length !== 0 && users.map(
                user => (<div key = {user.id}>
                    {user.complete ?
                    <span style={{textDecoration: 'line-through'}}>{user.email}</span>
                    : <span>{user.email}</span>}
                    <button onClick={deleteUser.bind(null, user.email)}>X</button>
                </div>)
            )}
        </Div>
    )
}
const Div = styled.div`
     text-align: center;
`