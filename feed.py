import yaml
import xml.etree.ElementTree as xml_tree

# Load the YAML file
try:
    with open('feed.yaml', 'r') as file:
        yaml_data = yaml.safe_load(file)
except FileNotFoundError:
    print("Error: 'feed.yaml' file not found.")
    exit(1)
except yaml.YAMLError as e:
    print(f"Error parsing YAML: {e}")
    exit(1)

# Create the RSS element
rss_element = xml_tree.Element('rss', {
    'version': '2.0',
    'xmlns:itunes': 'http://www.itunes.com/dtds/podcast-1.0.dtd',
    'xmlns:content': 'http://purl.org/rss/1.0/modules/content/'
})

channel_element = xml_tree.SubElement(rss_element, 'channel')

# Add title with default handling
title = yaml_data.get('title', 'Default Title')
xml_tree.SubElement(channel_element, 'title').text = title

# Write to XML
output_tree = xml_tree.ElementTree(rss_element)
output_tree.write('podcast.xml', encoding='UTF-8', xml_declaration=True)
