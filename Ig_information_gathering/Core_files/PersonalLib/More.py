#############################
#############################

Failed = "Something Worng"
isData = 'window._sharedData = {"config":'
Ghost1 = '<script type="text/javascript">window._sharedData = '
Ghost2 = ';</script>'

# Query
QueryUrl = "https://www.instagram.com/graphql/query/"
QueryHash= "?query_hash="
HashContent = "d4d88dc1500312af6f937f7b804c68c3"
QueryVariables = "&variables="
FixParameter = "&page=2"
QueryJson = {
	"user_id":"",
	"include_chaining":False,
	"include_reel":False,
	"include_suggested_users":False,
	"include_logged_out_extras":True,
	"include_highlight_reels":True,
	"include_live_status":True
}

# Websites
BaseLink1 = "https://webstagram.org/api?api_key=0&username="
BaseLink2 = "https://socialblade.com/instagram/user/"
Referer1 = "https://webstagram.org/report/"
Param1_1 = "&source=instagram"
Param1_2 = "/instagram"