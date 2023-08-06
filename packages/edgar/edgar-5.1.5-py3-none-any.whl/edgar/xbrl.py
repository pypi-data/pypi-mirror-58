from typing import Dict, List
import re
from datetime import datetime
from lxml import etree

def findnth(haystack, needle, n):
  parts= haystack.split(needle, n+1)
  if len(parts)<=n+1:
      return -1
  return len(haystack)-len(parts[-1])-len(needle)

class XBRL(etree.ElementBase):

  @classmethod
  def clean_tag(cls, elem):
    """
    Parse tag so 
      {http://fasb.org/us-gaap/2018-01-31}Assets
    becomes
      Assets
    """
    elem.tag = elem.tag[elem.tag.find("}")+1:]

  @classmethod
  def parse_context_ref(cls, context_ref):
    """
    Duration_1_1_2018_To_12_31_2018 becomes 2018-01-01 to 2018-12-31
    As_Of_12_31_2017 becomes 2017-12-31
    """
    context_ref_to_date_text = lambda s: datetime.strptime(s, "%m_%d_%Y").date().strftime("%Y-%m-%d")
    if context_ref.startswith("Duration"):
      if len(context_ref.split("_")) <= 9:
        from_date = context_ref_to_date_text(context_ref[len("DURATION")+1:context_ref.find("_To_")])
        to_date = context_ref_to_date_text(context_ref[context_ref.find("_To_")+4:])
        return {"from": from_date, "to": to_date}
      else:
        from_date = context_ref_to_date_text(context_ref[len("DURATION")+1:context_ref.find("_To_")])
        end_idx = findnth(context_ref, "_", 7)+1
        to_date = context_ref_to_date_text(context_ref[context_ref.find("_To_")+4:end_idx-1])
        return {"from": from_date, "to": to_date}

    elif context_ref.startswith("As_Of"):
      if len(context_ref.split("_")) <= 5:
        return {"from": context_ref_to_date_text(context_ref[len("As_Of")+1:])}
      else:
        end_idx = findnth(context_ref, "_", 4)+1
        from_date = context_ref_to_date_text(context_ref[len("As_Of")+1:end_idx-1])
        return {"from": from_date}
    else:
      return {"other": context_ref.split("_")[0]}

  @property
  def child(self):
    return self.getchildren()[0]

  @property
  def relevant_children(self):
    """
    Get children that are not `context`
    """
    return [child for child in self.child.getchildren() if not isinstance(child, etree._Comment) and "context" not in child.tag]

  @property
  def relevant_children_parsed(self):
    """
    Get children that are not `context`, `unit`, `schemaRef`
    """
    children = [child for child in self.child.getchildren() if not isinstance(child, etree._Comment) and "context" not in child.tag and "unit" not in child.tag and "schemaRef" not in child.tag]
    for elem in children:
      XBRL.clean_tag(elem)
    return children

class XBRLElement(etree.ElementBase):

  @property
  def child(self):
    return self.getchildren()[0]

  @property
  def attrib(self) -> Dict:
    return self.child.attrib

  @property
  def context_ref(self) -> Dict:
    return XBRL.parse_context_ref(self.attrib["contextRef"]) if self.attrib.get("contextRef") else {}

  @property
  def name(self):
    return ' '.join(re.findall('[A-Z][^A-Z]*', self.child.tag))

  @property
  def value(self) -> str:
    return self.child.text.replace("\n", "").strip() if self.child.text else ""

  def to_dict(self) -> Dict:
    return {
      "name": self.name,
      "value": self.value,
      "context_ref": self.context_ref
    }
