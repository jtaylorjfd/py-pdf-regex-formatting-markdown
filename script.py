
#Replace all white-space characters with the digit "9":

txt = """
1.7.12.8   A significant adverse visual effect (long-term and reversible) is predicted during the 
operations and maintenance phase of the Morgan Generation Assets for people using 
Douglas promenade and other similar publicly accessible, seafront/shoreline locations 
on the Isle of Man’s east coast where framed views of the Morgan Array Area are 
available at distances less than approximately 25km (e.g. Laxey). 
1.7.12.9   A significant adverse visual effect (long-term and reversible) is predicted for people 
onboard the Liverpool to Douglas and Heysham to Douglas ferries during the 
construction, operations and maintenance and decommissioning phases of the Morgan 
Generation Assets when passing the Morgan Array Area, travelling in either direction. 
The visual effect during construction and decommissioning would be less, temporary, 
short-term in duration and not significant beyond the Morgan Array Area.
1.7.12.10   Significant cumulative effects on seascape, landscape and visual resources as a result 
of the Morgan Generation Assets in combination with other projects and plans are 
not anticipated to arise during the construction, operations and maintenance and 
decommissioning phases.
Morgan Offshore Wind Project Generation Assets  |  Non-Technical Summary45
12687 - MORGAN GEN - PEIR - Non-Technical Summary_12pt_v7.indd   4512687 - MORGAN GEN - PEIR - Non-Technical Summary_12pt_v7.indd   45 28/03/2023   17:2328/03/2023   17:23
1.7.13  Socio-economics 
1.7.13.1   This chapter of the PEIR presents the assessment of the potential impact of the Morgan 
Generation Assets on socio-economics and community. There is a complexity with 
the socio-economic and community impacts associated with the Morgan Generation 
Assets’ activities primarily manifesting onshore. This chapter’s approach is focused on 
the 'source' of the impact, rather than the location of the physical infrastructure.
1.7.13.2   The socio-economics and community regional study area is linked to the selection 
of construction (and decommissioning), and operations and maintenance ports 
that will support the associated supply of a range of inputs and services for the 
Morgan Generation Assets. These ports, and their socio-economic catchment areas 
are anticipated to form focal points of impact on socio-economic and community 
receptors. The final selection of port facilities required for the Morgan Generation 
Assets has not yet been determined. The Applicant is exploring ports, supporting 
infrastructure and labour markets to understand the potential capabilities, capacities 
and availability that exists. Subject to these findings, a single port or multiple ports 
could be used to support primary elements of the construction, operations and 
maintenance, and decommissioning phases of the Morgan Generation Assets as part 
of a wider supply chain. 


"""
x = re.sub("\n\d+\.\d+\.\d+ ", "\nTEST", txt)
print(x)

y = re.search("\n\d+\.\d+\.\d+ ", txt)
