import axios from "axios";

const server = 'http://127.0.0.1:8000'
const header = {'Content-Type':'application/json'} //Restfull 데이터에 대한 설정 값
export const connect = () => axios.get(`${server}/api/connect`) 