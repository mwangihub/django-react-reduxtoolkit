import React from 'react'
import { useDispatch, useSelector } from 'react-redux'
import Api from '../../Api'
import { CsrfToken } from '../CsrfToken'
import { increment, login } from './AuthLoginReducer'


const AuthTest = () => {
    const count = useSelector(state => state.auth.count);
    const authLoader = useSelector(state => state.auth.authLoader);
    const authError = useSelector(state => state.auth.authError);
    const authData = useSelector(state => state.auth.authData);
    const dispatch = useDispatch();

    const handleSubmit = event => {
        event.preventDefault();
        const { email, password, csrfmiddlewaretoken } = event.target;
        console.log(email.value, password.value)
        const object = {
            email: email.value,
            password: password.value
        }
        dispatch(login(object))
    }
    return (
        <React.Fragment>

            <div className="container">
                <div className="d-flex justify-content-center">
                    <div className="col-8 my-3 pt-5">
                        <button onClick={e => dispatch(increment())} className="btn btn-sm w-100 btn-primary">Counter == {count}</button>
                        <form className='mt-5 pt-5' onSubmit={e => handleSubmit(e)}>
                            {authError && <div className="form-text my-3 text-danger">{JSON.stringify(authError)}</div>}
                            {authData && <div className="form-text my-3 text-success">{JSON.stringify(authData)}</div>}
                            <div className="mb-3">
                                <label className="form-label">csrfmiddlewaretoken</label>
                                <CsrfToken />
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
}

export default AuthTest