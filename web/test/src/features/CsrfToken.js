import React, { useEffect, useState } from 'react'
import Api from '../Api';
import Cookies from 'js-cookie'

export const CsrfToken = () => {
    const csrftoken_header = Cookies.get('csrftoken');
    const [csrftoken, setCsrftoken] = useState(csrftoken_header);
    const getCookie = name => {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    useEffect(() => {
        const fetchData = () => {
            Api.getCSRFToken()
                .then(response => {
                    console.log(response);
                }).catch(error => {
                    console.log(error);
                })
        }
        fetchData();
        console.log(csrftoken, csrftoken_header);
        setCsrftoken(getCookie("csrftoken"))
    }, [csrftoken, csrftoken_header])

    return (
        <input className="form-control" type="text" name="csrfmiddlewaretoken" value={csrftoken} disabled />
    )
}
