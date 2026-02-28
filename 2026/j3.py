ngoc = input()
minh = input()

n_count = 0
m_count = 0

n_pointer = 0
m_pointer = 0

while n_pointer < len(ngoc) and m_pointer < len(minh):

    if ngoc[n_pointer] == minh[m_pointer]:
        n_count += 1
        n_pointer += 1
        m_count += 1
        m_pointer += 1
    elif ngoc[n_pointer] == 'R' and minh[m_pointer] == 'G':
        n_count += 1
        m_pointer += 1
    elif ngoc[n_pointer] == 'G' and minh[m_pointer] == 'B':
        n_count += 1
        m_pointer += 1
    elif ngoc[n_pointer] == 'B' and minh[m_pointer] == 'R':
        n_count += 1
        m_pointer += 1
    elif minh[m_pointer] == 'R' and ngoc[n_pointer] == 'G':
        m_count += 1
        n_pointer += 1
    elif minh[m_pointer] == 'G' and ngoc[n_pointer] == 'B':
        m_count += 1
        n_pointer += 1
    elif minh[m_pointer] == 'B' and ngoc[n_pointer] == 'R':
        m_count += 1
        n_pointer += 1

print(n_count + (len(ngoc) - n_pointer))
print(m_count + (len(minh) - m_pointer))
