import axios from "axios";
import Cookies from "universal-cookie";


let http = (c_type = "application/json") => {
	let header = {
		"Content-type": c_type,
		'Accept': c_type,
	}
	return axios.create({
		baseURL: localStorage.getItem("host"),
		headers: header
	});
}

const logout = () => {
	return http().get("auth_urls/v1/logout/");
};

const checkAuthentication = () => {
	return http().get("auth_urls/v1/check-auth/")
};

const login = (email, password) => {
	const cookies = new Cookies();
	const createHttp = http();
	createHttp.defaults.headers.common['X-CSRFToken'] = cookies.get("csrftoken");
	return createHttp.post("auth_urls/v1/login/", {
		email,
		password,
	});
};

export const Api = {
	login,
	logout,
	checkAuthentication,
};

