from ywkd_tools.inner_service_apis.inner_service_apis import InnerServices, InnerService
from ywkd_tools.inner_service_apis.errors import InnerAPIError


@InnerServices.inner
class Participant(InnerService):
    """用户中心"""

    url = '/cperm/rpc/'

    def get_participant(self, participant_id):
        """
        获取参与利润分配的公司/团体详情
            @param: id
            @out: {     // 返回内容参考: http://yapi.yuwangkedao.com/project/251/interface/api/6233
                id: [id],
                participant_type: 类型,
                name: 名称,
                area_code_list: 区域列表,
                ...
            }
        """
        return self.rpc_client.get_participant(participant_id)
