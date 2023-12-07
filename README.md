# Getting Started with Latest Django-React redux toolkit

## Overview Django REST Framework
Django REST framework (DRF) is a powerful and flexible toolkit for building Web APIs in Django. It provides a set of tools and abstractions to make it easier to build and consume APIs in a Django application. Here are some key features and concepts associated with Django REST framework:

1. **Serializers:** Serializers allow complex data types, such as querysets and model instances, to be converted to Python data types that can be easily rendered into JSON. Serializers also provide deserialization, allowing parsed data to be converted back into complex types.

2. **Views and ViewSets:** DRF provides class-based views and viewsets that make it easy to organize your API logic. Views and viewsets handle HTTP methods (GET, POST, PUT, DELETE, etc.) and map them to corresponding methods on the view or viewset.

3. **Authentication and Permissions:** DRF includes built-in support for various authentication methods (token, session, OAuth, etc.) and permissions (allowing or denying access based on user roles).

4. **Routers:** Routers simplify the URL configuration for your API by automatically wiring up the necessary URL patterns for your viewsets.

5. **Authentication Classes:** DRF supports various authentication methods, and you can specify them in your settings.

   ```python
   REST_FRAMEWORK = {
       'DEFAULT_AUTHENTICATION_CLASSES': [
           'rest_framework.authentication.TokenAuthentication',
           'rest_framework.authentication.SessionAuthentication',
       ],
   }
   ```
6. **Permissions Classes:** You can define permissions to control access to your API views.

7. **Pagination and Filtering:** DRF provides built-in support for paginating and filtering querysets.

8. **Browsable API:** DRF includes a browsable API, making it easy to explore and interact with your API through a web interface.

   ![Browsable API](https://www.django-rest-framework.org/img/browsable-api.png)
Redux Toolkit is a set of utilities and conventions for reducing the boilerplate code that comes with using Redux. It includes tools for simplifying common Redux use cases and improving developer experience. When working with React, using Redux Toolkit in conjunction with React Redux provides an even more streamlined development experience. Below, I'll provide an overview of how to use React Redux Toolkit.

## Setting Up Redux Toolkit

1. **Install Redux Toolkit and React Redux:**
   ```bash
   npm install @reduxjs/toolkit react-redux
   ```

2. **Create a Redux Store:**
   Create a file to configure your Redux store

3. **Create Reducers:**
   In the `reducers` directory, create separate files for each slice of your state and use the `createSlice` function from Redux Toolkit

4. **Combine Reducers:**
   Combine all your reducers in the `reducers/index.js` file

### Integrating with React:

1. **Provide the Redux Store:**
   Wrap your application with the `Provider` from `react-redux` and provide the Redux store:
   ```javascript
   // index.js or App.js
   import React from 'react';
   import ReactDOM from 'react-dom';
   import { Provider } from 'react-redux';
   import store from './store';
   import App from './App';

   ReactDOM.render(
     <Provider store={store}>
       <App />
     </Provider>,
     document.getElementById('root')
   );
   ```

2. **Use Redux Toolkit Hooks:**
   Utilize the hooks provided by Redux Toolkit for accessing state and dispatch actions in your components.
