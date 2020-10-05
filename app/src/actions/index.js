import axios from 'axios'
export const FETCH_LIBRARY = 'FETCH_LIBRARY';

export function fetchLibrary() {
    const request = axios.get('/libraries/');
    return {
        type: FETCH_LIBRARY,
        payload: request
    }
}