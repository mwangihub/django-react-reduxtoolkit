import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";
import Api from "../../Api";


const initialState = {
    count: 0,
    authLoader: false,
    authError: null,
    authData: null
}

export const login = createAsyncThunk("auth/login", (object) => {
    console.log(object);
    const { email, password } = object;
    return Api.login(email, password)
        .then(response => response.data)
})

export const authLogin = createSlice({
    name: "auth",
    initialState,
    reducers: {
        increment: state => {
            state.count += 1;
        }
    },
    extraReducers(builder) {
        builder.addCase(login.pending, (state, action) => {
            state.authLoader = true
            state.authError = null
            state.authData = null
        }).addCase(login.fulfilled, (state, action) => {
            console.log(action);
            state.authLoader = false
            state.authError = null
            state.authData = action.payload
            state.count = 200
        }).addCase(login.rejected, (state, action) => {
            state.authLoader = false
            state.authError = action.error.message
            state.authData = null
            state.count = 404
        })
    }
})


export const { increment } = authLogin.actions;
export default authLogin.reducer;