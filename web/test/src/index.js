import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import reportWebVitals from './reportWebVitals';
import { HashRouter } from "react-router-dom";
import { Provider } from 'react-redux';
import { store } from './app/store';
import Utils from './utils/utils';

const root = document.getElementById('root');
if (root) {
Utils.setItemLocalStorage([["host", root.dataset.host],])
  ReactDOM.createRoot(root)
    .render(
      <Provider store={store}>
        <HashRouter>
          <App {...root.dataset}/>
        </HashRouter>
      </Provider>
    );
}


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
