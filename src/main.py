from word_lists import agent_list, test_list

if __name__ == '__main__':
    print ("Agent list:")
    print (*map(lambda x: x.rep, agent_list))
    print (*map(lambda x: x.unique, agent_list))
    print ("Test list:")
    print (*map(lambda x: x.rep, test_list))


