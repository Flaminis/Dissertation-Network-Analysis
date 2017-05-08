from mygraph import MyGraph
import vk
def vk_graph(my_id=57573111):
    appid = '5989878'
    login = 'kopjasar@gmail.com'
    password = 'Kopjasar102030'
    session = vk.AuthSession(appid, login, password, scope='friends')
    vk_api = vk.API(session)
    mygraph = MyGraph()
    me = vk_api.users.get(user_ids=my_id,fields='city,photo_400_orig,domain')
    mygraph.add_single_node(0,info=me)
    my_friends_ids = vk_api.friends.get(user_id=my_id)
    my_friends_full = vk_api.friends.get(user_id=my_id,fields='city,photo_400_orig,domain')
    active_friends = [my_id]
    counter = 1
    # print my_friends_full uncomment for info
    for friend in my_friends_full:
        if friend.get('deactivated')==None:
            active_friends.append(friend.get('user_id'))
            mygraph.add_single_node(active_friends.index(friend.get('user_id')),info=friend)
    mutual = vk_api.friends.getMutual(source_uid=my_id,target_uids=active_friends)
    for m in mutual:
        source = m.get('id')
        source_id = active_friends.index(source)
        print source_id
        mygraph.add_single_edge(0,source_id,weight=1)
        for target in m.get('common_friends'):
            if target in active_friends:
                target_id = active_friends.index(target)
                mygraph.add_single_edge(source_id,target_id,weight=1)
    return mygraph
