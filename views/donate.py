import streamlit as st

def load_view():
	st.markdown(
	"""
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        <h1>Donate Now</h1>
        	<ul>
        		<li>
        			<a role="button" href="https://www.coolearth.org/donate/usd/">Cool Earth: Protecting the World’s Rainforests</a>
            	</li>
            	<li>
        			<a role="button" href="https://donate.catf.us/page/39127/donate/1">Clean Air Task Force: Reducing Carbon Emissions</a>
            	</li>
            	<li>
        			<a role="button" href="https://secure.ucsusa.org/JuXeEefnxEqkc7b6uwrzeg2?MS=topnav&_gl=1*1k3thz2*_ga*NzY4NzU5MzgwLjE2NjE0NDgyMDA.*_ga_VB9DKE4V36*MTY2MTQ0ODE5OS4xLjEuMTY2MTQ0OTE0MS4wLjAuMA..">Union of Concerned Scientists: Using Science to Make Change Happen</a>
            	</li>
            	<li>
        			<a role="button" href="https://carbon180.org/donate">Carbon180: Zero. Then Negative.</a>
            	</li>
            	<li>
        			<a role="button" href="https://www.greenpeace.org.uk/support-us/">Greenpeace: Defending the Natural World</a>
            	</li>
            	<li>
        			<a role="button" href="https://give.rainforest-alliance.org/give/291977/?&_ga=2.12788023.1805348368.1661448317-1211936639.1661448317#!/donation/checkout?c_src=MDW22BX&c_src2=2202mwebfndmainnav">Rainforest Alliance: Fighting Deforestation and Climate Change</a>
            	</li>
            	<li>
        			<a role="button" href="https://donate.earthisland.org/page/39685/donate/1">Earth Island: Standing up for Wilderness</a>
            	</li>
            	<li>
        			<a role="button" href="https://teamtrees.org/">Team Trees: Mr.Beast and Mark Rober's $1 to Plant a Tree</a>
            	</li>
            	<li>
        			<a role="button" href="https://teamseas.org//">Team Seas: Mr.Beast and Mark Rober's $1 to Remove a Pound of Trash from the Ocean</a>
            	</li>
	""", unsafe_allow_html=True)