from Products.CMFCore.utils import getToolByName


def uninstall(self):
    setup_tool = getToolByName(self, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile(
        'profile-collective.js.throttledebounce:uninstall',
        ignore_dependencies=True)
