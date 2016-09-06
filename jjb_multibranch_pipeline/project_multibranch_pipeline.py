import xml.etree.ElementTree as XML
import jenkins_jobs.modules.base


class MultibranchPipeline(jenkins_jobs.modules.base.Base):
    sequence = 0

    def root_xml(self, data):
        xml_parent = XML.Element('org.jenkinsci.plugins.workflow.multibranch.WorkflowMultiBranchProject', {'plugin': 'workflow-multibranch'})
        return xml_parent
