import axios from 'axios'

export function request(baseURL){
    const axiosFactory = axios.create({
        baseURL: baseURL,
        timeout: 5000
    })
    axiosFactory.interceptors.response.use((res) => res.data, (e) => Promise.reject(e))
    axiosFactory.interceptors.request.use((config) => config, (e) => Promise.reject(e))
    return axiosFactory
}


