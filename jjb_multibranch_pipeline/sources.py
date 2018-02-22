import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
import xml.etree.ElementTree as XML
import jenkins_jobs.modules.base
from jenkins_jobs.modules.scm import SCM


class MultibranchPipeline(jenkins_jobs.modules.base.Base):
    sequence = 0

    component_type = 'multibranch-pipeline'
    component_list_type = 'multibranch-pipeline'

    def gen_xml(self, xml_parent, data):
        sources = data.get(self.component_type, {})

        source_definition = 'source' in sources
        definition_type = 'MultiBranchProject$BranchSourceList' if source_definition else ''

        xml_sources = XML.SubElement(
            xml_parent,
            'sources',
            {
                'plugin': 'branch-api',
                'class': 'jenkins.branch.' + definition_type
            }
        )
        xml_sources = XML.SubElement(xml_sources, 'data', {})
        xml_sources = XML.SubElement(xml_sources, 'jenkins.branch.BranchSource', {})
        xml_sources = XML.SubElement(xml_sources, 'source', {
            'plugin': 'git',
            'class': 'jenkins.plugins.git.GitSCMSource'
        })

        if source_definition:
            source = sources.get('source', [{}])[0]
            gitData = source.get('git', {})
            XML.SubElement(xml_sources, 'id').text = gitData.get('id', '')
            XML.SubElement(xml_sources, 'remote').text = gitData.get('remote', '')
            XML.SubElement(xml_sources, 'credentialsId').text = gitData.get('credentials-id', '')
            XML.SubElement(xml_sources, 'includes').text = gitData.get('includes', '')
            XML.SubElement(xml_sources, 'excludes').text = gitData.get('excludes', '')
            XML.SubElement(xml_sources, 'ignoreOnPushNotifications').text = gitData.get('ignore-on-push-notifications', 'false')
