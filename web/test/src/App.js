import React from "react";
import { useLocation, useNavigate } from 'react-router-dom';
import { connect } from 'react-redux'
import Utils from './utils/utils';
import { Route, Routes } from 'react-router-dom';
import AuthTest from "./features/auth/AuthTest";
import { authLogin } from "./features/auth/AuthLoginReducer";
import AppHOC from "./AppHOC";
//"build": "DEL /F/Q/S build > nul && RMDIR /Q/S build && react-scripts build && Xcopy .\build ..\build /E /H /C /I",
class BaseApp extends React.Component {

  render() {
    return (
      <Routes>
        <Route path="/" element={<AuthTest />}></Route>
      </Routes>
    )
  }
}


const App = (props) => {
  const navigate = useNavigate()
  const location = useLocation()
  const properties = Utils.objectUpdate(props, {
    navigate, location
  })
  return <BaseApp {...properties} />
}

const finalApp = AppHOC(App, {})

const mapStateToProps = state => ({
  authState: state.auth,
});
const mapDispatchToProps = { authLogin };
export default connect(mapStateToProps, mapDispatchToProps)(finalApp);

