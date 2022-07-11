import axios from "axios";
import Cookies from 'js-cookie'

const csrftoken_header = Cookies.get('csrftoken');
let http = (token = null, c_type = "application/json") => {
    let header = {
        "Content-type": c_type,
        'Accept': c_type,
        'X-CSRFToken': csrftoken_header,
    }
    return axios.create({
        baseURL: localStorage.getItem("host"),
        headers: header
    });
}

const login = (email, password) => {
    return http().post("auth_urls/v1/login/", { 
        email, 
        password,
     });
}
const getCSRFToken = () => {
    return http().get("auth_urls/get_csrf_token/");
}

const Api = {
    login,
    getCSRFToken,
};
export default Api