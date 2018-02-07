import urllib.request

all_city_url = 'http://m.weather.com.cn/data5/city.xml'
p_content = urllib.request.urlopen(all_city_url).read()
provinces = p_content.split(',')
result = 'city = {\n'
city_url = 'http://m.weather.com.cn/data3/city%s.xml'
for p in provinces:
    p_code = p.split('|')[0]
    p_url = city_url % p_code
    c_content = urllib.request.urlopen(p_url).read()
    cities = c_content.split(',')
    for c in cities:
        c_code = c.split('|')[0]
        c_url = city_url % c_code
        d_content = urllib.request.urlopen(c_url).read()
        districts = d_content.split(',')
        for d in districts:
            d_pair = d.split('|')
            d_code = d_pair[0]
            name = d_pair[1]
            d_url = city_url % d_code
            code_content = urllib.request.urlopen(d_url).read()
            code = code_content.split('|')[1]
            line = "    '%s': '%s',\n" % (name, code)
            result += line
            print(name + ':' + code)
result += '}'
f = open('primer/weather/test/city.py', 'w')
f.write(result)
f.close()