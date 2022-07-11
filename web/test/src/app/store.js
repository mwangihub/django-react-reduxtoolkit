import { configureStore } from "@reduxjs/toolkit";
import authLoginReducer from "../features/auth/AuthLoginReducer";

export const store = configureStore({
    reducer: {
        auth: authLoginReducer
    },
})
