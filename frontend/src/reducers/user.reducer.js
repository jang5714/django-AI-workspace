import { act } from "react-dom/test-utils"

const initialState = {users: [], user: {}}
export const addUserAction = user => ({type: "ADD_USER", payload: user})
export const toggleUserAction = userId => ({type: 'TOGLE_USER', payload: userId})
export const deleteUserAction = userId => ({type: 'DELETE_USER', payload: userId})
const userReducer = (state = initialState, action) => {
    switch(action.type){
        case 'ADD_USER' : return {...state, users:[...state.users, action.payload]}
        case 'TOGLE_USER' : return {...state, users:state.users.map(user => (user.email === action.payload)
                                                                    ? {...user, complete: !user.complete}: user)}

        case 'DELETE_USER' : return {...state, users:state.users.filter(user => user.email != action.payload)}
        default : return state

    }
}

export default userReducer