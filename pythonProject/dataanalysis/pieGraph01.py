import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Malgun Gothic'

slices = [1, 2, 3, 4]
hobbies = ['잠자기', '외식', '영화감상', '운동']
mycolors = ['blue', '#6AFF00', 'yellow', '#FF003C']

plt.pie(x=slices, labels=hobbies, shadow=True, explode=(0, 0.1, 0, 0),
        colors=mycolors, autopct='%1.2f%%', startangle=90, counterclock=False)

# plt.legend() 메소드의 loc 매개변수 항목 참조 요망
plt.legend(loc=4)

filename = 'pieGraph01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + '파일이 저장되었습니다')
plt.show()