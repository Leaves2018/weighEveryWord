import weigh2
import weigh3

text = """There is an enormous difference in the ways in which various public officials respond to public pressures, and in the means and methods they employ to deal with them. The best possess understanding of the forces that must be taken into account, determination not to be swerved from the path of public interest, a willingness to make enemies along with a gift for avoiding them and faith that public support will be forthcoming for the correct course. The poorest are overhesitant, evasive, preoccupied with their relationships with their colleagues, superiors, the press or the political support on which they lean. They will make no move unless the gallery is packed. They confront all embarrassments with a stale general formula."""
uf1, uk1 = weigh2.first(text)
uf2, uk2 = weigh3.first(text)
print("========weigh2========")
for i in uk1:
    print(i.get_name())
print("========weigh3========")
for i in uk2:
    print(i.get_name())
