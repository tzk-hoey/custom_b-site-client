<template>
<el-card :style="{width:(isAll? '90%': '420px')}">
    <div class="dynamic-item">
        <span class="user">
            <img v-lazy-img="data.modules.module_author.face">
        </span>
        <span class="info-content">
            <div class="info">
                {{ data.modules.module_author.name }}&nbsp;&nbsp;在&nbsp;&nbsp;{{ dayjs.unix(data.modules.module_author.pub_ts).format('YY-MM-DD HH:mm:ss') }}&nbsp;&nbsp;{{ data.modules.module_author.pub_action? data.modules.module_author.pub_action: action+"了动态" }}
            </div>
            <div class="content" v-if="data.modules.module_dynamic.desc && isAll">
                <a v-for="(node, index) in data.modules.module_dynamic.desc.rich_text_nodes" :key="data.id_str+'-a'+index.toString()" :href="node.jump_url" target="_blank">{{ node.text }}</a>
            </div>
            <div class="pics"></div>
            <div class="major" v-if="data.modules.module_dynamic.major">
                <div class="major-pics" v-if="data.modules.module_dynamic.major.draw">
                    <PictureGroup :data="data.modules.module_dynamic.major.draw.items"/>
                </div>
                <div class="major-archive" v-if="data.modules.module_dynamic.major.archive">
                    <VideoCard :data="{
                        floating: '👀'+data.modules.module_dynamic.major.archive.stat.play+' 🗯️'+data.modules.module_dynamic.major.archive.stat.danmaku,
                        floatingBottom: data.modules.module_dynamic.major.archive.duration_text,
                        url: data.modules.module_dynamic.major.archive.jump_url,
                        title: data.modules.module_dynamic.major.archive.title,
                        subtitle: data.modules.module_dynamic.major.archive.badge.text,
                        picture: data.modules.module_dynamic.major.archive.cover
                    }"/>
                </div>
                <div class="major-live" v-if="data.modules.module_dynamic.major.live_rcmd">
                    <VideoCard :data="{
                        floating: '👀'+data.modules.module_dynamic.major.live_rcmd.content.live_play_info.watched_show.num,    
                        floatingBottom: '',
                        url: 'https:'+data.modules.module_dynamic.major.live_rcmd.content.live_play_info.link,
                        title: data.modules.module_dynamic.major.live_rcmd.content.live_play_info.title,
                        subtitle: data.modules.module_dynamic.major.live_rcmd.content.live_play_info.parent_area_name,
                        picture: data.modules.module_dynamic.major.live_rcmd.content.live_play_info.cover
                    }"/>
                </div>
            </div>
            <div class="addition"></div>
            <div class="origin" v-if="data.orig">
                <DynamicItem :data="data.orig"/>
            </div>
            <div class="stat" v-if="data.modules.module_stat && isAll">
                <el-button-group>
                    <el-button>
                        <el-icon><Share/></el-icon>{{ data.modules.module_stat.forward.count }}
                    </el-button>
                    <el-button>
                        <el-icon><Comment/></el-icon>{{ data.modules.module_stat.comment.count }}
                    </el-button>
                    <el-button>
                        <el-icon><CircleCheck/></el-icon>{{ data.modules.module_stat.like.count }}
                    </el-button>
                </el-button-group>
            </div>
            <div class="three-points"></div>
        </span>
    </div>
</el-card>
</template>

<!-- 
动态数据对象结构
data.
    id_str  #作为key使用
    modules.
        module_author.
            avatar.
                face
            name
            pub_action  #动作，如“投稿了视频”
            pub_ts      #动作时间戳
        module_dynamic.
            desc.
                rich_text_nodes[
                    item.
                        jump_url    #超链接才有，否则为空
                        orig_text
                        text
                        type
                ]   #富文本节点数组，包含多个以文本为主的元素
                text    #全部转化为普通文本的形式
            major.
                draw.   #图片组
                    items[
                        item.
                            height
                            width
                            src
                    ]   
                archive.    #视频对象
                live_rcmd.
                    content #直播数据json字符串
                    
            additional.
                reverse. #附件内容
                    title   #附件标题
                    jump_url    #附件链接，可为空
                    desc1   #可为直播时间
        module_stat.
            comment., forward., like.  #评论、转发、点赞对象
                count
                forbidden
                status  #点赞专属，表示自己是否点赞
    orig.   #有这个表明是一个转发


 -->

<script setup>
import dayjs from 'dayjs'
import {ref} from 'vue'

const props = defineProps({
    data: { type: Object, required: true},
    isAll: { type: Boolean, default: true}
})

// preprocess live info
if (props.data.modules.module_dynamic.major && props.data.modules.module_dynamic.major.live_rcmd){
    props.data.modules.module_dynamic.major.live_rcmd.content = JSON.parse(props.data.modules.module_dynamic.major.live_rcmd.content)
}

const action = ref(props.data.orig? '转发': '发布')
</script>

<style scoped lang="scss">
.el-card{
    display: inline-block;
    margin-bottom: 10px;
    margin-right: 10px;
}
.dynamic-item{
    width: 100%;
    display: flex;
    justify-content: flex-start;
    align-content: flex-start;
    align-items: normal;

    .user{
        margin-right: 10px;

        img{
            height: 60px;
            width: 60px;
        }
    }

    .info-content{
        width: 100%;
        margin-left: 10px;

        > div{
            margin-bottom: 10px;
        }
    }

    .info{
        font-size: larger;
    }

    .content{
        margin-top: 5px;
        a{
            margin-right: 2px;
            white-space: pre-line;
        }
    }

    .major{
        margin-top: 10px;
    }
}
</style>