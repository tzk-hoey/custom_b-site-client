import { request } from '@/utils/request'

export function useMyinfoAPI(baseURL){

    const axiosFactory = request(baseURL)

    function getMyinfoAPI(){
        const config = {
            url: '/myinfo',
            method: 'GET',
        }
        return axiosFactory(config)
    }
    return {
        getMyinfoAPI,
    }
}