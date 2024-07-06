import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { authLoginAction } from "../index";
import { useNavigate } from "react-router-dom";

export const LoginComponent = React.memo(function Login() {
	const authLoader = useSelector(state => state.AuthLoginReducer.authLoader);
	const authError = useSelector(state => state.AuthLoginReducer.authError);
	const authData = useSelector(state => state.AuthLoginReducer.authData);
	const dispatch = useDispatch();
	const navigate = useNavigate()

	useEffect(() => {
		if (authData) {
			navigate("/profile", { replace: true })
		}
	}, [authData, navigate]);

	const handleSubmit = event => {
		event.preventDefault();
		const { email, password } = event.target;
		const object = {
			email: email.value,
			password: password.value,
		};
		dispatch(authLoginAction(object));
	};

	return (
		<React.Fragment>
			<div className="container">
				<div className="d-flex justify-content-center">
					<div className="col-8 my-3 pt-5">
						<form className='mt-5 pt-5' onSubmit={e => handleSubmit(e)}>
							{authError && <div className="form-text my-3 text-danger">{JSON.stringify(authError)}</div>}
							{authData && <div className="form-text my-3 text-success">{JSON.stringify(authData)}</div>}
							<div className="mb-3">
							</div>
							<div className="mb-3">
								<label className="form-label">Email address</label>
								<input type="email" name='email' className="form-control" />
							</div>
							<div className="mb-3">
								<label className="form-label">Password</label>
								<input type="text" name='password' className="form-control" />
							</div>
							<button type="submit" disabled={authLoader} className="btn btn-warning btn-sm w-100">Submit</button>
						</form>

					</div>
				</div>
			</div>
		</React.Fragment>
	)
});