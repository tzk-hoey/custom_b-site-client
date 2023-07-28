import { request } from '@/utils/request'

export function useMessageAPI(baseURL){

    const axiosFactory = request(baseURL)

    function getReplyAPI(id=undefined, time=undefined){
        const config = {
            url: '/message/replytome',
            method: 'GET',
        }
        if (id && time){
            config.params = {
                id,
                time
            }
        }
        return axiosFactory(config)
    }

    function getApprovalAPI(id=undefined, time=undefined){
        const config = {
            url: '/message/approvaltome',
            method: 'GET',
        }
        if (id && time){
            config.params = {
                id,
                time
            }
        }
        return axiosFactory(config)
    }

    return {
        getReplyAPI,
        getApprovalAPI
    }
}