import { request } from '@/utils/request'

export function useConfigAPI(baseURL){

    const axiosFactory = request(baseURL)

    function getCookiesAPI(){
        return axiosFactory({
            url: '/cookies',
            method: 'GET'
        })
    }
    function postCookiesAPI(data){
        return axiosFactory({
            url: '/cookies',
            method: 'POST',
            data,
            headers: {
                'Content-Type': 'application/json'
            }
        })
    }
    function refreshCookiesAPI(){
        return axiosFactory({
            url: '/cookies',
            method: 'GET',
            params: {
                operation: 'refresh'
            }
        })
    }
    return {
        getCookiesAPI,
        postCookiesAPI,
        refreshCookiesAPI
    }
}