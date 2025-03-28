// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.SUPAVISOR_NATIVE.Tenants
{
    [SUPAVISOR_NATIVEResourceType("supavisor-native:tenants:Tenant")]
    public partial class Tenant : global::Pulumi.CustomResource
    {
        /// <summary>
        /// SELECT rolname, rolpassword FROM pg_authid WHERE rolname=$1
        /// </summary>
        [Output("authQuery")]
        public Output<string?> AuthQuery { get; private set; } = null!;

        /// <summary>
        /// Database name
        /// </summary>
        [Output("dbDatabase")]
        public Output<string> DbDatabase { get; private set; } = null!;

        /// <summary>
        /// Database host
        /// </summary>
        [Output("dbHost")]
        public Output<string> DbHost { get; private set; } = null!;

        /// <summary>
        /// Database port
        /// </summary>
        [Output("dbPort")]
        public Output<int> DbPort { get; private set; } = null!;

        [Output("enforceSsl")]
        public Output<bool?> EnforceSsl { get; private set; } = null!;

        /// <summary>
        /// External ID
        /// </summary>
        [Output("externalId")]
        public Output<string?> ExternalId { get; private set; } = null!;

        [Output("insertedAt")]
        public Output<string?> InsertedAt { get; private set; } = null!;

        /// <summary>
        /// auto
        /// </summary>
        [Output("ipVersion")]
        public Output<string?> IpVersion { get; private set; } = null!;

        [Output("requireUser")]
        public Output<bool?> RequireUser { get; private set; } = null!;

        /// <summary>
        /// your.domain.com
        /// </summary>
        [Output("sniHostname")]
        public Output<string?> SniHostname { get; private set; } = null!;

        [Output("tenant")]
        public Output<Outputs.TenantProperties> TenantValue { get; private set; } = null!;

        [Output("updatedAt")]
        public Output<string?> UpdatedAt { get; private set; } = null!;

        [Output("upstreamSsl")]
        public Output<bool?> UpstreamSsl { get; private set; } = null!;

        /// <summary>
        /// none
        /// </summary>
        [Output("upstreamVerify")]
        public Output<string?> UpstreamVerify { get; private set; } = null!;

        [Output("users")]
        public Output<ImmutableArray<Outputs.User>> Users { get; private set; } = null!;


        /// <summary>
        /// Create a Tenant resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Tenant(string name, TenantArgs args, CustomResourceOptions? options = null)
            : base("supavisor-native:tenants:Tenant", name, args ?? new TenantArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Tenant(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("supavisor-native:tenants:Tenant", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/phillarson-xyz/pulumi-supavisor-native",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Tenant resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Tenant Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Tenant(name, id, options);
        }
    }

    public sealed class TenantArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// External ID of the tenant
        /// </summary>
        [Input("externalId")]
        public Input<string>? ExternalId { get; set; }

        [Input("tenant", required: true)]
        public Input<Inputs.TenantPropertiesArgs> TenantValue { get; set; } = null!;

        public TenantArgs()
        {
        }
        public static new TenantArgs Empty => new TenantArgs();
    }
}
