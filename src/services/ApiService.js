import axios from "axios";

export function getpatient(){
    return axios.get('http://localhost:8000/patient/')
        .then(res => res.data);
}