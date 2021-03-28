from xml.dom.minidom import parseString


class XMLAssertions(object):

    def _extract_element(self, xml_str, element_path):
        doc = parseString(xml_str)
        elements = element_path.split('.')
        parent = doc
        for element_name in elements:
            sub_elements = parent.getElementsByTagName(element_name)
            if len(sub_elements) == 0:
                msg = "No element matching '%s' found using XML string '%s'" % (element_name, element_path)
                raise AssertionError(msg)
            parent = sub_elements[0]
        return parent

    def assertXMLElementText(self, xml_str, value, element_path):
        """
        Assert that an XML string contains an element
        with value matching that passed.
        """
        element = self._extract_element(xml_str, element_path)
        self.assertEquals(value, element.firstChild.data)

    def assertXMLElementAttributes(self, xml_str, attributes, element_path):
        """
        Assert that an XML element contains a given set of attributes
        """
        element = self._extract_element(xml_str, element_path)
        for attribute, value in attributes.items():
            self.assertEquals(value, element.attributes[attribute].value)
         