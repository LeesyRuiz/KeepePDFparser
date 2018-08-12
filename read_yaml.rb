require 'streak-ruby'
require 'yaml'
require 'json'
require 'httparty'
 
# x = YAML.load_file('/Users/lisyruiz/Documents/KeepePDFparser/data.yml')
# puts x.inspect


 

 


Streak.api_key = '95bf522aaa6348298d7cef4cc9571628'
pipeline_key = 'agxzfm1haWxmb29nYWVyMAsSDE9yZ2FuaXphdGlvbiIJa2VlcGUuY29tDAsSCFdvcmtmbG93GICAgMCInYAKDA'





box = Streak::Box.create(pipeline_key, { :name => 'OMG' })
 
 
# puts box.inspect
puts box.key



# BoxID = box['key']


#what will nameing convenction be 

#get the box id.... from streak 
# "boxKey": "agxzfm1haWxmb29nYWVyLAsSDE9yZ2FuaXphdGlvbiIJa2VlcGUuY29tDAsSBENhc2UYgICAwrCznwoM",

# updated customer field s



