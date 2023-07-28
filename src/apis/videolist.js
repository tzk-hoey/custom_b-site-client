import { request } from '@/utils/request'

export function useVideoListAPI(baseURL){

    const axiosFactory = request(baseURL)

    function getPopularAPI(pn=1, ps=20){
        return axiosFactory({
            url: '/popular',
            method: 'GET',
            params: {
                pn,
                ps
            }
        })
    }
    return {
        getPopularAPI,
    }
}